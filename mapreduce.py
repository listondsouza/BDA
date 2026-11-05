print("""
HADOOP MAPREDUCE PRACTICAL – DISTINCT WORD COUNT
================================================

1. CHECK REQUIREMENTS (Ubuntu Terminal)
---------------------------------------
java -version
javac -version
hadoop version
hdfs dfs -ls /
jps

Make sure Hadoop services are running.

2. CREATE PROJECT AND INPUT FILE
--------------------------------
mkdir -p ~/wordcount
cd ~/wordcount
nano input.txt

Enter:
hello world
hello hadoop
big data
hello world

Save: Ctrl + O, Enter, Ctrl + X

3. CREATE MAPPER
----------------
nano DistinctWordMapper.java

Enter:
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DistinctWordMapper
    extends Mapper<Object, Text, Text, IntWritable> {

    private static final IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException {

        String line = value.toString();
        String[] words = line.split("\\\\s+");

        for (String w : words) {
            word.set(w);
            context.write(word, one);
        }
    }
}

Save and exit nano.

4. CREATE REDUCER
-----------------
nano DistinctWordReducer.java

Enter:
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class DistinctWordReducer
    extends Reducer<Text, IntWritable, Text, IntWritable> {

    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException {

        result.set(1);
        context.write(key, result);
    }
}

Save and exit nano.

5. CREATE DRIVER
----------------
nano DistinctWordDriver.java

Enter:
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class DistinctWordDriver {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Distinct Word Count");

        job.setJarByClass(DistinctWordDriver.class);
        job.setMapperClass(DistinctWordMapper.class);
        job.setReducerClass(DistinctWordReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

Save and exit nano.

6. COMPILE JAVA FILES AND CREATE JAR
------------------------------------
Make sure you are in:
cd ~/wordcount

Create classes folder:
mkdir -p classes

Compile:
javac -classpath "$(hadoop classpath)" -d classes *.java

Create JAR:
jar -cvf distinctword.jar -C classes .

Check files:
ls

Expected files:
DistinctWordMapper.java
DistinctWordReducer.java
DistinctWordDriver.java
input.txt
classes
distinctword.jar

7. UPLOAD INPUT FILE TO HDFS
----------------------------
hdfs dfs -mkdir -p /wordcount/input
hdfs dfs -put input.txt /wordcount/input/
hdfs dfs -ls /wordcount/input

8. RUN MAPREDUCE PROGRAM
------------------------
hadoop jar distinctword.jar DistinctWordDriver /wordcount/input /wordcount/output

IMPORTANT: The output directory must not already exist.

To run again, remove old output first:
hdfs dfs -rm -r /wordcount/output

Then run the JAR command again.

9. VIEW OUTPUT
--------------
hdfs dfs -ls /wordcount/output
hdfs dfs -cat /wordcount/output/part-r-00000

Expected output:
big       1
data      1
hadoop    1
hello     1
world     1

Count distinct words:
hdfs dfs -cat /wordcount/output/part-r-00000 | wc -l

Expected count:
5

10. EXECUTION LOGIC
-------------------
Mapper: splits each line into words and emits (word, 1).
Shuffle and Sort: groups identical words together.
Reducer: writes each unique word once.
Final output: 5 distinct words.
""")
