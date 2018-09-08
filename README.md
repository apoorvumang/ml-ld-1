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
Smoothing factor (ALPHA): 0.1



Run time local:

Training:
Preprocessing 1h 15min 23 sec (214997 documents)
Counting: 1min 46sec

Prediction:
Preprocessing: 6min 1sec (29997 documents)
Prediction: 2min 9sec (29997 documents)





Mapreduce:

Default:
start: 2018-09-06 22:04:27,317 INFO mapreduce.Job:  map 100% reduce 0%
end: 2018-09-06 22:08:10,617 INFO mapreduce.Job:  map 100% reduce 100%
diff: around 3min 43sec

Reducers = 1
start: 2018-09-06 22:12:01,909 INFO mapreduce.Job:  map 100% reduce 0%
end: 2018-09-06 22:16:12,243 INFO mapreduce.Job:  map 100% reduce 100%

2018-09-06 22:14:47,200 INFO mapreduce.Job:  map 100% reduce 0%
2018-09-06 22:16:12,243 INFO mapreduce.Job:  map 100% reduce 100%


Reducers = 2
2018-09-06 22:34:26,136 INFO mapreduce.Job:  map 100% reduce 0%
2018-09-06 22:35:54,173 INFO mapreduce.Job:  map 100% reduce 100%

Reducers = 10
2018-09-06 22:42:29,997 INFO mapreduce.Job:  map 100% reduce 0%
2018-09-06 22:43:27,021 INFO mapreduce.Job:  map 100% reduce 100%
