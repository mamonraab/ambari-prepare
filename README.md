# ambari-prepare

these py script will do the fellow
first if you need help run these py
https://youtu.be/i_INe5EmiZA
1- setup your eth device and set static ip and change host name

and will install these pkg
wget curl openssl openssh tar zip scp java-1.8.0-openjdk java-1.8.0-openjdk-devl ntp deltarpm gcc perl
http://public-repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.4.2.0/ambari.repo

than you should do the fallwoing
1- make all node see each other by host name not only ip
you can sure that from /etc/hosts
nano /etc/hosts

2- in  main node the ambari server node do these cmd 

yum -y install ambari-server
ambari-server setup
ambari-server start

chkconfig  ambari-server 

in agent node doe

nano /etc/ambari-agent/conf/ambari-agent.ini

[server]

hostname=<your.ambari.server.hostname>

url_port=8440

secured_url_port=8441

 
ambari-agent start

The agent registers with the Server on start. 


==============================
الشرح العربي
اولا  شغل كما في الفيديو
https://youtu.be/i_INe5EmiZA
ثم
السكربت سيقوم بمجمل مهام التثبيت والاعداد والبرامجيات المطلوبة
وحسب الفيديو  التالي لمعرفة كيفية تشغيل السكربت
fعد تشغيل السكربت وانتهائة
يتم عمل نسختين كلون او اكثر من النسخة التي نصبنا عليها السكربت
سنقوم بعمل التالي 
نحتاج 1 نود لتكون نيم نود الرئيسي
والباقي والذي هو كاقل عدد 2 نود ان تكون الداتا نود
يجب ان تتاكد من ان كل نود ترى الاخرى عبر نطاق الدومين وليس فقط الايبي ويمكن ذلك عبر الملف التالي

/etc/hosts

وايضا تحتاج ان تكتب التالي بالنود الرئيسية

yum -y install ambari-server
ambari-server setup
ambari-server start

chkconfig  ambari-server 

في العميل تكتب
nano /etc/ambari-agent/conf/ambari-agent.ini

[server]

hostname=<your.ambari.server.hostname>

url_port=8440

secured_url_port=8441

 
ambari-agent start


بعدها اتصل بلامباري سيرفر عبر المتصفح
mainboxip:8080
