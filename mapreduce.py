print("""
HADOOP MAPREDUCE PRACTICAL – DISTINCT WORD COUNT
================================================

AIM:
To implement a MapReduce program in Java that finds
the distinct words present in an input text file.

EXPECTED RESULT:
Input contains:
hello world
hello hadoop
big data
hello world

Distinct words:
big
data
hadoop
hello
world

Total distinct words = 5


================================================
1. UNDERSTAND WHAT WE ARE DOING
================================================

We will perform these steps:

1. Create a project folder.
2. Create an input text file.
3. Write the Mapper Java program.
4. Write the Reducer Java program.
5. Write the Driver Java program.
6. Compile all Java files.
7. Create a JAR file.
8. Upload input file to HDFS.
9. Execute the MapReduce program.
10. Display the final output.

IMPORTANT:
We use THREE Java files:
- DistinctWordMapper.java
- DistinctWordReducer.java
- DistinctWordDriver.java


================================================
2. CHECK REQUIREMENTS (UBUNTU TERMINAL)
================================================

Open Ubuntu Terminal.

Shortcut:
Ctrl + Alt + T

Check Java:
java -version

-> Displays installed Java version.

Check Java compiler:
javac -version

-> Checks whether Java compiler is installed.

Check Hadoop:
hadoop version

-> Displays installed Hadoop version.

Check HDFS:
hdfs dfs -ls /

-> Displays files and folders in HDFS root.

Check running Java/Hadoop processes:
jps

-> Displays running Java processes.

Common Hadoop processes:
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager


IF JAVA IS NOT INSTALLED:
sudo apt update
sudo apt install default-jdk -y

Check again:
java -version
javac -version


IF HADOOP SERVICES ARE NOT RUNNING:

Start HDFS:
start-dfs.sh

Start YARN:
start-yarn.sh

Check:
jps

IMPORTANT:
Do not reinstall Hadoop if it is already configured.
Use the Hadoop installation provided in your lab.


================================================
3. CREATE PROJECT FOLDER
================================================

Go to your HOME directory:
cd ~

-> Moves to the home directory.

Create project folder:
mkdir -p wordcount

-> Creates a folder named wordcount.
-> -p avoids an error if the folder already exists.

Enter the folder:
cd ~/wordcount

-> Opens the wordcount folder.

Check current location:
pwd

-> Displays the current directory.

Check files:
ls

-> Displays files in the folder.

At this stage, the folder should be empty.


================================================
4. CREATE INPUT TEXT FILE
================================================

Create a file:
nano input.txt

-> Opens the nano text editor.
-> We use nano to create and edit text files.

TYPE THE FOLLOWING:

hello world
hello hadoop
big data
hello world

SAVE THE FILE:

1. Press Ctrl + O.
2. Press Enter.
3. Press Ctrl + X.

Check the file:
cat input.txt

-> Displays the contents of input.txt.

Expected:
hello world
hello hadoop
big data
hello world


================================================
5. CREATE MAPPER PROGRAM
================================================

What is a Mapper?

Mapper reads the input file line by line.
It separates each line into individual words.

For every word, it produces:
(word, 1)

Example:
hello world

Mapper output:
(hello, 1)
(world, 1)

CREATE FILE:

nano DistinctWordMapper.java

TYPE THIS CODE:

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

SAVE:
Ctrl + O -> Enter -> Ctrl + X

CHECK FILE:
cat DistinctWordMapper.java

-> Displays the Mapper code.

MAPPER FUNCTION:
1. Reads one line.
2. Converts the line into a String.
3. Splits the line into words.
4. Sends each word with value 1.


================================================
6. CREATE REDUCER PROGRAM
================================================

What is a Reducer?

Reducer receives words grouped by Hadoop.

Example:
hello -> [1, 1, 1]
world -> [1, 1]

Our objective is DISTINCT WORD COUNT.
Therefore, we write every unique word only once.

CREATE FILE:

nano DistinctWordReducer.java

TYPE THIS CODE:

import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class DistinctWordReducer
    extends Reducer<Text, IntWritable, Text, IntWritable> {

    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context)
        throws IOException, InterruptedException {

        result.set(1);
        context.write(key, result);
    }
}

SAVE:
Ctrl + O -> Enter -> Ctrl + X

CHECK FILE:
cat DistinctWordReducer.java

-> Displays the Reducer code.

REDUCER FUNCTION:
1. Receives each unique word.
2. Receives the values belonging to that word.
3. Sets the output value to 1.
4. Writes the word only once.

IMPORTANT:
This is DISTINCT WORD COUNT.
It does NOT calculate the actual frequency of each word.


================================================
7. CREATE DRIVER PROGRAM
================================================

What is a Driver?

Driver is the main program.
It connects Mapper, Reducer and Hadoop.

It tells Hadoop:
- Which Mapper to use.
- Which Reducer to use.
- Where input is located.
- Where output should be stored.

CREATE FILE:

nano DistinctWordDriver.java

TYPE THIS CODE:

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

SAVE:
Ctrl + O -> Enter -> Ctrl + X

CHECK FILE:
cat DistinctWordDriver.java

DRIVER FUNCTION:
1. Creates Hadoop configuration.
2. Creates a MapReduce job.
3. Sets Mapper class.
4. Sets Reducer class.
5. Sets output key and value types.
6. Sets input and output paths.
7. Starts the job and waits for completion.


================================================
8. CHECK ALL THREE JAVA FILES
================================================

Run:
ls

Expected files:

input.txt
DistinctWordMapper.java
DistinctWordReducer.java
DistinctWordDriver.java

If any file is missing, create it before continuing.


================================================
9. CREATE CLASSES FOLDER
================================================

Run:
mkdir -p classes

-> Creates a folder named classes.
-> Compiled Java class files will be stored here.

Check:
ls

You should now see:
classes
input.txt
DistinctWordMapper.java
DistinctWordReducer.java
DistinctWordDriver.java


================================================
10. COMPILE JAVA PROGRAMS
================================================

Make sure you are inside:
~/wordcount

Check:
pwd

Compile all three Java files:

javac -classpath "$(hadoop classpath)" -d classes *.java

EXPLANATION:

javac
-> Java compiler.

-classpath
-> Specifies the libraries required for compilation.

$(hadoop classpath)
-> Gets Hadoop library locations.

-d classes
-> Saves compiled files inside classes folder.

*.java
-> Compiles all Java files in the folder.

IF SUCCESSFUL:
No error message should appear.

Check compiled files:
find classes -type f

Expected:
DistinctWordMapper.class
DistinctWordReducer.class
DistinctWordDriver.class

Note:
Some additional inner class files may also appear.


================================================
11. CREATE JAR FILE
================================================

What is a JAR?

JAR means Java Archive.
It packages compiled Java class files into one file.

Run:

jar -cvf distinctword.jar -C classes .

EXPLANATION:

jar
-> Java archive command.

-c
-> Creates a new JAR.

-v
-> Displays files being added.

-f
-> Specifies JAR filename.

distinctword.jar
-> Name of the JAR file.

-C classes
-> Uses the classes folder.

.
-> Includes everything inside that folder.

CHECK:
ls

Expected:

input.txt
DistinctWordMapper.java
DistinctWordReducer.java
DistinctWordDriver.java
classes
distinctword.jar

Check JAR contents:
jar -tf distinctword.jar

-> Displays files inside the JAR.


================================================
12. CREATE INPUT DIRECTORY IN HDFS
================================================

What is HDFS?

HDFS = Hadoop Distributed File System.

It stores files in Hadoop.

Create input directory:

hdfs dfs -mkdir -p /wordcount/input

-> Creates wordcount/input directory in HDFS.

Check directory:

hdfs dfs -ls /wordcount

-> Displays contents of wordcount directory.


================================================
13. UPLOAD INPUT FILE TO HDFS
================================================

Make sure you are inside:
~/wordcount

Check:
pwd

Upload input file:

hdfs dfs -put input.txt /wordcount/input/

-> Copies input.txt from Ubuntu local filesystem
   to HDFS.

Check uploaded file:

hdfs dfs -ls /wordcount/input

Expected:
input.txt

Display HDFS input:

hdfs dfs -cat /wordcount/input/input.txt

-> Displays the input file stored in HDFS.


================================================
14. EXECUTE MAPREDUCE PROGRAM
================================================

Run:

hadoop jar distinctword.jar DistinctWordDriver /wordcount/input /wordcount/output

EXPLANATION:

hadoop jar
-> Executes a Hadoop JAR file.

distinctword.jar
-> Our compiled program.

DistinctWordDriver
-> Main class of the program.

 /wordcount/input
-> Input directory in HDFS.

 /wordcount/output
-> Output directory in HDFS.

IMPORTANT:
Hadoop will automatically:
1. Read the input file.
2. Execute the Mapper.
3. Shuffle and sort Mapper output.
4. Execute the Reducer.
5. Store the final result in HDFS.

WAIT UNTIL THE JOB COMPLETES.

Successful execution should show:
Job completed successfully.


================================================
15. VIEW FINAL OUTPUT
================================================

Check output directory:

hdfs dfs -ls /wordcount/output

-> Displays generated output files.

Display result:

hdfs dfs -cat /wordcount/output/part-r-00000

EXPECTED OUTPUT:

big       1
data      1
hadoop    1
hello     1
world     1

Count distinct words:

hdfs dfs -cat /wordcount/output/part-r-00000 | wc -l

Expected:
5

-> wc -l counts the number of output lines.
-> Each line represents one distinct word.


================================================
16. RUN THE PROGRAM AGAIN
================================================

IMPORTANT:

Hadoop does not allow an existing output directory.

If you run the same program again, remove the old output:

hdfs dfs -rm -r /wordcount/output

-> Deletes the old output directory from HDFS.

Now execute again:

hadoop jar distinctword.jar DistinctWordDriver /wordcount/input /wordcount/output


================================================
17. UNDERSTAND MAPREDUCE EXECUTION
================================================

INPUT:

hello world
hello hadoop
big data
hello world

MAPPER OUTPUT:

hello -> 1
world -> 1
hello -> 1
hadoop -> 1
big -> 1
data -> 1
hello -> 1
world -> 1

SHUFFLE AND SORT:

big -> [1]
data -> [1]
hadoop -> [1]
hello -> [1, 1, 1]
world -> [1, 1]

REDUCER OUTPUT:

big -> 1
data -> 1
hadoop -> 1
hello -> 1
world -> 1

FINAL RESULT:
5 DISTINCT WORDS.


================================================
18. COMMON ERRORS AND SOLUTIONS
================================================

ERROR 1: javac command not found

Meaning:
Java compiler is not installed.

Solution:
sudo apt install default-jdk -y


ERROR 2: hadoop command not found

Meaning:
Hadoop is not configured or PATH is incorrect.

Solution:
Check Hadoop installation and environment variables.


ERROR 3: NameNode is not running

Meaning:
HDFS service is stopped.

Solution:
start-dfs.sh

Check:
jps


ERROR 4: Input directory does not exist

Meaning:
Input file was not uploaded to HDFS.

Solution:
hdfs dfs -ls /wordcount/input

Upload again:
hdfs dfs -put input.txt /wordcount/input/


ERROR 5: Output directory already exists

Meaning:
Previous output is still present.

Solution:
hdfs dfs -rm -r /wordcount/output


ERROR 6: Could not find or load main class

Meaning:
Driver class or JAR packaging may be incorrect.

Check:
jar -tf distinctword.jar

Recompile and recreate JAR if necessary.


ERROR 7: Compilation errors

Meaning:
Java code or Hadoop classpath may be incorrect.

Check:
hadoop classpath

Then compile again:
javac -classpath "$(hadoop classpath)" -d classes *.java


================================================
19. IMPORTANT COMMANDS – QUICK REVISION
================================================

CHECK JAVA:
java -version
javac -version

CHECK HADOOP:
hadoop version
jps

CREATE FOLDER:
mkdir -p wordcount

OPEN FOLDER:
cd ~/wordcount

CREATE FILE:
nano input.txt

DISPLAY FILE:
cat input.txt

CREATE CLASSES FOLDER:
mkdir -p classes

COMPILE:
javac -classpath "$(hadoop classpath)" -d classes *.java

CREATE JAR:
jar -cvf distinctword.jar -C classes .

CHECK JAR:
jar -tf distinctword.jar

CREATE HDFS DIRECTORY:
hdfs dfs -mkdir -p /wordcount/input

UPLOAD FILE:
hdfs dfs -put input.txt /wordcount/input/

CHECK HDFS:
hdfs dfs -ls /wordcount/input

RUN MAPREDUCE:
hadoop jar distinctword.jar DistinctWordDriver /wordcount/input /wordcount/output

DISPLAY OUTPUT:
hdfs dfs -cat /wordcount/output/part-r-00000

COUNT DISTINCT WORDS:
hdfs dfs -cat /wordcount/output/part-r-00000 | wc -l

DELETE OLD OUTPUT:
hdfs dfs -rm -r /wordcount/output


================================================
20. EXIT / STOP SERVICES
================================================

Exit terminal:
exit

OPTIONAL:
If you started Hadoop services and need to stop them:

Stop YARN:
stop-yarn.sh

Stop HDFS:
stop-dfs.sh

Do not stop shared lab services unless instructed.


================================================
IMPORTANT PRACTICAL NOTES
================================================

1. Always check Java and Hadoop before starting.
2. Create all three Java files in the same folder.
3. Compile before creating the JAR.
4. Upload input file to HDFS before running the job.
5. Output directory must not already exist.
6. Check final output using hdfs dfs -cat.
7. This program counts DISTINCT words, not total frequency.

END OF PRACTICAL
""")
