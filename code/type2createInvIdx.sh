hadoop fs -put /home/jmistry2/Project-InvertedIndex/dataset/210000.txt /user/jmistry2/input/

hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
	   -input /user/jmistry2/input/preproc_reviews.dat \
	   -output /user/jmistry2/output/createInvIdx2 \
	   -mapper /home/jmistry2/Project-InvertedIndex/type2createInvIdx_map1.py \
	   -reducer /home/jmistry2/Project-InvertedIndex/type2createInvIdx_reduce1.py
	   
hadoop fs -get /user/jmistry2/output/createInvIdx2/part-00000 /home/jmistry2/Project-InvertedIndex/out_save/createInvIdxStep1.dat



hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
	  -D stream.num.map.output.key.fields=2 \
	  -D stream.num.reduce.output.key.fields=1 \
	  -D mapred.text.key.partitioner.options=-k1,1 \
	  -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	  -D mapred.text.key.comparator.options="-k1n -k2n" \
      -input /user/jmistry2/output/createInvIdx2/part-00000 \
      -output /user/jmistry2/output/createInvIdx2_2 \
      -mapper /home/jmistry2/Project-InvertedIndex/type2createInvIdx_map2.py \
      -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	  -reducer /home/jmistry2/Project-InvertedIndex/type2createInvIdx_reduce2.py


hadoop fs -get /user/jmistry2/output/createInvIdx2_2/part-00000 /home/jmistry2/Project-InvertedIndex/out_save/createInvIdxStep2_3.dat

hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
	   -input /user/jmistry2/output/createInvIdx2_2/part-00000 \
	   -output /user/jmistry2/output/createInvIdx2_3 \
	   -mapper /home/jmistry2/Project-InvertedIndex/type2createInvIdx_map3.py \
	   -reducer /home/jmistry2/Project-InvertedIndex/type2createInvIdx_reduce3.py

hadoop fs -get /user/jmistry2/output/createInvIdx2_3/part-00000 /home/jmistry2/Project-InvertedIndex/out_save/createInvIdxStep2_4.dat


hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
	   -input /user/jmistry2/output/createInvIdx2_2/part-00000 \
	   -output /user/jmistry2/output/createInvIdx2_3 \
	   -mapper /home/jmistry2/Project-InvertedIndex/type2createInvIdx_map3.py \
	   -reducer /home/jmistry2/Project-InvertedIndex/dummy.py