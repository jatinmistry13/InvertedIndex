hadoop fs -put /home/jmistry2/Project-InvertedIndex/preprocessed_reviews.dat /user/jmistry2/input/

hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
	   -input /user/jmistry2/input/preprocessed_reviews.dat \
	   -output /user/jmistry2/output/createInvIdx \
	   -mapper /home/jmistry2/Project-InvertedIndex/createInvIndex_map.py \
	   -reducer /home/jmistry2/Project-InvertedIndex/createInvIndex_reduce.py
	   
hadoop fs -get /user/jmistry2/output/createInvIdx/part-00000 /home/jmistry2/Project-InvertedIndex/out_save/InvertedIndex.dat
