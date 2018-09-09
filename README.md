# ml-ld-1
Assignment 1 for ML-LD course


Very small dataset:
Local:


Stemming - ALPHA = 0.01
Training set: 8370/10497
Test set: 780/1497
Devel: 1730/2997

<!-- Lemming - ALPHA = 0.01
Training set: 8213/10500
Test set: 773/1500
Devel: 1685/3000


Lemming - ALPHA = 0.01 - With class distribution
Training set: 8238/10500
Test set: 782/1500
Devel: 1694/3000 -->

Stemming - ALPHA = 0.01 - With class distribution
Training set: 8403/10500
Test set: 778/1500 (785 with ALPHA 0.1, 787 with 0.1 and no class distribution)
Devel set:


Full dataset:
Local:

Stemming:
Training set: 181846/33151 (84.58%) with ALPHA = 0.1 2nd try: 179895/35102(83.67) (ALPHA 0.1)
Test set: 23883/29997 (79.62%) ALPHA = 0.01, 24045(80.15%) with ALPHA = 0.1 2nd try:  (23950/29997)(79.84)
3rd try: 24037/29997 (80.13%)
Devel set: 47392/14105 (77.06%) with ALPHA = 0.1  2nd try: 47053(76.5%)



Without removing stop words:
Test set: ALPHA = 0.1 23532 (78.44)


Parameters:
Words: 211577
Classes: 50
Class distribution for each class
Smoothing factor (ALPHA): 0.1



Run time local:

Training:
Preprocessing 1h 15min 23 sec (214997 documents)
Counting: 1min 46sec

Prediction:
Preprocessing: 6min 1sec (29997 documents)
Prediction: 2min 9sec (29997 documents)





Mapreduce:

Test accuracy: 23244/(23244+6753)  77.84
Train accuracy: 171158/(171158+43839) 79.6
Development accuracy: 45287/(45287+16210) 73.6

With stemming and stopwords:
Test accuracy: 24032/(24032+5965) 80.11
Train accuracy: 183527/(183527+31470) 85.36
Development accuracy: 47415/(47415+14082) 77.10

Timings:
reducers = 1
18/09/09 17:55:56 INFO mapreduce.Job:  map 100% reduce 0%
18/09/09 17:56:58 INFO mapreduce.Job:  map 100% reduce 100%
62 seconds

reducers = 2
18/09/08 14:30:17 INFO mapreduce.Job:  map 100% reduce 0%
18/09/08 14:30:57 INFO mapreduce.Job:  map 100% reduce 100%
40 seconds

reducers = 5
18/09/08 14:26:02 INFO mapreduce.Job:  map 100% reduce 0%
18/09/08 14:26:20 INFO mapreduce.Job:  map 100% reduce 100%
18 seconds

reducers = 8
18/09/09 18:47:59 INFO mapreduce.Job:  map 100% reduce 0%
18/09/09 18:48:13 INFO mapreduce.Job:  map 100% reduce 100%
14 seconds

reducers = 10
18/09/08 14:23:19 INFO mapreduce.Job:  map 100% reduce 0%
18/09/08 14:23:31 INFO mapreduce.Job:  map 100% reduce 100%
12 seconds
