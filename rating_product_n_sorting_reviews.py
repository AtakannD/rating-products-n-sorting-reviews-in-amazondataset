import pandas as pd
import math
import scipy.stats as st
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_csv(
    r'C:\Users\atakan.dalkiran\PycharmProjects\Rating Product & Sorting Reviews in Amazon\amazon_review.csv')
df.head()

# Task 1.1
df["overall"].value_counts()
avg_rate = df["overall"].sum() / df["asin"].value_counts()

# Task 1.2

df["reviewTime"] = pd.to_datetime(df['reviewTime'], format="%Y-%m-%d")
current_date = df["reviewTime"].max()
df["reviewTimeDiff"] = (current_date - df["reviewTime"]).dt.days
pd.qcut(df["reviewTimeDiff"], 4).value_counts()
df.loc[df["reviewTimeDiff"] <= 280, "overall"].mean() * 29 / 100 + \
    df.loc[(df["reviewTimeDiff"] > 280) & (df["reviewTimeDiff"] <= 430), "overall"].mean() * 26.5 / 100 + \
    df.loc[(df["reviewTimeDiff"] > 430) & (df["reviewTimeDiff"] <= 600), "overall"].mean() * 23.5 / 100 + \
    df.loc[df["reviewTimeDiff"] > 600, "overall"].mean() * 21 / 100

# Task 1.3
df.loc[df["reviewTimeDiff"] <= 280, "overall"].mean() > \
df.loc[(df["reviewTimeDiff"] > 280) & (df["reviewTimeDiff"] <= 430), "overall"].mean() > \
df.loc[(df["reviewTimeDiff"] > 430) & (df["reviewTimeDiff"] <= 600), "overall"].mean() > \
df.loc[df["reviewTimeDiff"] > 600, "overall"].mean()

# Task 2.1
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]

# Task 2.2


def score_up_down_diff(up, down):
    return up - down


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


def wilson_lower_bound(up, down, confidence=0.95):
    """
    Calculation of Wilson Lower Bound Score

    - The lower limit of the confidence interval to be calculated for the Bernaulli parameter p is accepted as the WLB score.
    - The score to be calculated is used for product ranking.
    - Note:
    If the scores are between 1-5, 1-3 are marked as negative, 4-5 as positive and can be made suitable for bernaulli.
    This also creates some problems. For this reason, it is necessary to apply the bayesian average rating.

    Parameters
    ----------
    up : int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)
df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

# Task 2.3
df.sort_values("wilson_lower_bound", ascending=False).head(20)
