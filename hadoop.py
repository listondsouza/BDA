print("""
HADOOP PRACTICAL – INSTALLATION CHECKS AND HDFS COMMANDS
========================================================

1. CHECK WHETHER HADOOP IS INSTALLED (Ubuntu Terminal)
------------------------------------------------------
java -version
hadoop version
hdfs version
jps
echo $HADOOP_HOME
ls $HADOOP_HOME/etc/hadoop

If the commands work and Hadoop is configured, skip installation and go to Section 4.

2. INSTALLATION – ONLY IF HADOOP IS MISSING
-------------------------------------------
Install Java and SSH:
sudo apt update
sudo apt install openjdk-11-jdk openssh-server openssh-client rsync -y

Create Hadoop user:
sudo adduser hadoop
sudo usermod -aG sudo hadoop
su - hadoop

Configure passwordless SSH:
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
ssh localhost
# If asked to continue connecting, type yes.
exit

Download and extract Hadoop 3.3.6:
cd ~
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 hadoop

Set environment variables:
nano ~/.bashrc

Add:
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HOME=$HOME/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

Save and reload:
source ~/.bashrc
hadoop version

Configure Java:
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
# Set:
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

Configure core-site.xml:
nano $HADOOP_HOME/etc/hadoop/core-site.xml
# Inside the existing <configuration> element:
<property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
</property>

Configure hdfs-site.xml:
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
# Inside <configuration>:
<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>
<property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///home/hadoop/hadoopdata/namenode</value>
</property>
<property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///home/hadoop/hadoopdata/datanode</value>
</property>

Configure mapred-site.xml:
nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
# Inside <configuration>:
<property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
</property>

Configure yarn-site.xml:
nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
# Inside <configuration>:
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>

Format NameNode ONLY for first-time setup:
hdfs namenode -format

Start Hadoop:
start-dfs.sh
start-yarn.sh

Verify:
jps

Expected processes can include:
NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager

IMPORTANT: These installation commands assume a fresh Hadoop 3.3.6 setup and /home/hadoop. If the lab machine already has configured Hadoop, do not replace its existing configuration or format its NameNode.

3. OPEN HADOOP WEB INTERFACES
-----------------------------
Open Firefox:
NameNode: http://localhost:9870
YARN ResourceManager: http://localhost:8088

4. HDFS PRACTICAL COMMANDS
--------------------------
Create directory:
hdfs dfs -mkdir /college

List HDFS root:
hdfs dfs -ls /

Create local file:
echo "Hello Hadoop" > input.txt

Create empty HDFS file:
hdfs dfs -touchz /college/empty.txt

Upload local file:
hdfs dfs -put input.txt /college/
# Alternative:
hdfs dfs -copyFromLocal input.txt /college/

View file:
hdfs dfs -cat /college/input.txt

Download from HDFS:
hdfs dfs -get /college/input.txt downloaded.txt

Copy inside HDFS:
hdfs dfs -cp /college/input.txt /college/copy.txt

Move inside HDFS:
hdfs dfs -mv /college/copy.txt /college/newfile.txt

Check disk usage:
hdfs dfs -du /college
hdfs dfs -du -s /college

View file statistics:
hdfs dfs -stat "%n %b bytes" /college/input.txt

Set replication:
hdfs dfs -setrep 1 /college/input.txt

Delete file:
hdfs dfs -rm /college/newfile.txt

Delete directory:
hdfs dfs -rm -r /college

Verify:
hdfs dfs -ls /

5. USEFUL DISTINCTION
---------------------
Local filesystem commands: ls, cat, mkdir
HDFS commands: hdfs dfs -ls, hdfs dfs -cat, hdfs dfs -mkdir
""")
