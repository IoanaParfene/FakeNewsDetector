# FakeNewsDetector
&nbsp;&nbsp;&nbsp;&nbsp;A **Python** implementation of a Romanian **Fake News** detection tool for [UAIC](https://www.uaic.ro/en/)'s [Faculty of Computer Science Iasi](https://www.info.uaic.ro/en/presentation/)'s **Natural Language Processing** course. <br>
&nbsp;&nbsp;&nbsp;&nbsp;The **article** about its **creation** and **performance** can be found [here](https://github.com/IoanaParfene/FakeNewsDetector/blob/main/Documentation.pdf).

## Motivation
&nbsp;&nbsp;&nbsp;&nbsp;This **project** aims to obtain **data** for an article that documents the process of using several **classifiers** in order to identify **Fake News** from Romanian news web sites. <br>
&nbsp;&nbsp;&nbsp;&nbsp;**Algorithms** are tested on different **vectorization** procedures, lengths of tokenized vocabularies and test data sizes. The sought after information pertains to the **accuracy** and time of each **classification** run.

## Data Distribution
&nbsp;&nbsp;&nbsp;&nbsp; **True News**(200 000 words)
  * [ProTV](https://stirileprotv.ro/) - 42,000 
  * [Digi24](https://www.digi24.ro/) -  70,000
  * [Libertatea](https://www.libertatea.ro/) - 42,000 
  * [Realitatea](https://www.realitatea.net/) - 46,000
  
&nbsp;&nbsp;&nbsp;&nbsp; **Fake News**(200 000 words)
  * [TimesNewRoman](https://www.timesnewroman.ro/) - 8,000
  * [Cațavencii](https://www.catavencii.ro/) - 99,000
  * [7lucruri](https://7lucruri.ro/) - 56,000
  * [TimpuriGrele](https://www.timpurigrele.ro/) - 37,000
  
## Method
&nbsp;&nbsp;&nbsp;&nbsp;
The **process** makes use of the Romanian **Fake and True News** articles **scraped** from **real and satire** news sites. The text is **preprocessed** through tokenization and stemming, **vectorized** and passed through several **classifiers** in order to find the one that yields the best **accuracy** and/or **time**.

<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126017533-60faa28d-ec3e-4e86-96b2-3378b88ccc60.png" width="600" height="600">
</p>

## Results
&nbsp;&nbsp;&nbsp;&nbsp;Each **classifier** was tested on a custom number of **runs**, **vectorized** with TF-IDF or Bag of Words, using 200, 1000 or all of the words in the **vocabulary**, from either 10% or 20% **test data**. 
### Naive Bayes Classifier
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126018705-02a5e813-e8c2-4437-8308-2317ec1f9f38.png" width="900" height="180">
</p>

### Passive Aggressive Classifier
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126018961-d6ec2c44-5ab1-4926-b563-7090e5d28fd6.png" width="900" height="180">
</p>

### Logistic Regression
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126018700-5e3c2257-8510-429c-b6ff-1d3ca7dc0e7e.png" width="900" height="180">
</p>

### Support Vector Machines
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126018703-c19cdcee-dd26-4cb6-816c-33bdadc7b70d.png" width="900" height="180">
</p>

### Decision Tree Classifier
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019161-c0f4deb1-f1b1-47ef-ae0c-41178d943186.png" width="900" height="180">
</p>

### Random Forest Classifier
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019170-77542051-ed4f-4dfe-a981-0de9b57e32ca.png" width="900" height="180">
</p>

### Ada Boost Classifier
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019147-b00a512e-494a-4e39-aa17-2c17c7fff08e.png" width="900" height="180">
</p>

### Voting Classifier - Random Forest, Logistic Regression, KNN
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019138-ab82637b-eaa0-4d31-b927-f379bd1b248a.png" width="900" height="180">
</p>

### Voting Classifier - Naive Bayes, Logistic Regression, Passive Aggressive
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019137-992163bf-9b7f-4754-ab51-74c223880cca.png" width="900" height="180">
</p>

### Voting Classifier - Naive Bayes, Random Forest, Passive Aggressive
<p align="center">
 <img src="https://user-images.githubusercontent.com/57050677/126019348-f5c00ffb-1f9c-4517-a150-3f945b8452b5.png" height="180">
</p>
