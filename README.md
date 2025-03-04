 Sentiment Analysis in Python

 Overview:
 
      *This project performs sentiment analysis on tweets by counting positive and negative words.
      *It processes user input, removes punctuation, and checks against predefined word lists to determine the sentiment score.

Features:

      #Cleans input text by removing punctuation
      #Identifies and counts positive and negative words
      #Calculates an overall sentiment score (positive - negative)
      #Uses predefined word lists for accurate classification

 How It Works:
 
     1)The user enters a tweet.
     2)The program removes punctuation from the text.
     3)It compares words against predefined positive and negative word lists.
     4)It outputs:
        -The number of positive words
        -The number of negative words
        -The final sentiment score (positive - negative)

Example:

      Enter a tweet: I love coding, but debugging is frustrating!  
      Tweet: I love coding, but debugging is frustrating!  
      Positive words: 1  
      Negative words: 1  
      Overall: 0  

      
Future Improvements:

     *Implement machine learning models for better sentiment detection.
     *Support for real-time tweet analysis via Twitter API.
     *Expand word lists for more accurate results.
