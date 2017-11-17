FROM rhel
#RUN sudo yum -y update
#RUN sudo yum -y install unzip
#RUN sudo yum -y install hostname
#RUN yum -y update && \
#yum -y install sudo openssh-clients telnet unzip hostname && \
#yum clean all
#RUN apt-get install unzip
#RUN apt-get install hostname
RUN mkdir -p /opt/ics/secureagent
ADD agent64_install.bin /opt/ics/secureagent
WORKDIR /opt/ics/secureagent/
CMD ['./opt/ics/secureagent/agent64_install.bin','/opt/ics/secureagent']
WORKDIR /opt/ics/secureagent/apps/agentcore
CMD ['./opt/ics/secureagent/apps/agentcore/infaagent','startup']
RUN sleep 30s
WORKDIR /opt/ics/secureagent/apps/agentcore
CMD ['./consoleAgentManager.sh','configure','nidhi.kalamkar@hughes.com.sit2','reset123']
CMD echo 'success'
