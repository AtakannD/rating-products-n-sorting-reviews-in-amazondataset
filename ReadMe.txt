*Rating Product & Sorting Reviews in Amazon*


1. Business Problem

One of the most important problems in e-commerce is the correct calculation of the points given to the products after sales. The solution to this problem is for the e-commerce site; Delivering greater customer satisfaction means product prominence for sellers and a seamless shopping experience for buyers.
Another problem is the correct ordering of the comments given to the products. The prominence of misleading comments will cause both financial loss and loss of customers, as it will directly affect the sale of the product. In solving these two basic problems, e-commerce site and sellers will increase their sales, while customers will complete their purchasing journey without any problems.


2. Story of Dataset

This dataset, which includes Amazon product data, includes product categories and various metadata. The product with the most reviews in the electronics category has user ratings and reviews.


3. Variables of Dataset

reviewerID: User id
asin: Id of product
reviewerName: Username
helpful: Helpful rating rating
reviewText: Review
overall: Product rating
summary: Evaluation summary
unixReviewTime: Evaluation time
reviewTime: Review time
Rawday_diff: Number of days since evaluation
helpful_yes: The number of times the review was found helpful
total_vote: Number of votes given to the review


Task 1: Calculate the Average Rating according to the current comments and compare it with the existing average rating.

	Step 1: Calculating the average score of the product.
	Step 2: Calculating the weighted average score by date.
	Step 3: In weighted scoring, comparing the average of each time period.


Task 2: Specify 20 reviews to be displayed on the product detail page for the product.

	Step 1: Generating the helpful_no variable for better understanding comment is helpful or not.
	Step 2: Calculating the score_pos_neg_diff, score_average_rating and wilson_lower_bound scores.
	Step 3: Identifying 20 interpretations and interpret the results.






