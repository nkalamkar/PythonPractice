FROM rhel
#RUN yum -y update
#RUN yum -y install unzip
#RUN yum -y install hostname
RUN yum -y update && \
yum -y install sudo openssh-clients telnet unzip hostname && \
yum clean all
#RUN apt-get install unzip
#RUN apt-get install hostname
RUN mkdir -p /opt/ics/secureagent
ADD agent64_install.bin /opt/ics/secureagent
WORKDIR /opt/ics/secureagent/
RUN ['/opt/ics/secureagent/agent64_install.bin','/opt/ics/secureagent']
WORKDIR /opt/ics/secureagent/apps/agentcore
RUN ['/apps/agentcore/infaagent','startup']
RUN sleep 50s
CMD ['./consoleAgentManager','configure','nidhi.kalamkar@hughes.com.sit2','reset123']
