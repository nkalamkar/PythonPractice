FROM rhel
RUN mkdir -p /opt/ics/secureagent
RUN cp /tmp/agent64_install.bin /opt/ics/secureagent
WORKDIR /opt/ics/secureagent/
RUN ['./agent64_install.bin','/opt/ics/secureagent']
WORKDIR /opt/ics/secureagent/apps/agentcore
RUN ['./apps/agentcore/infaagent','startup']
RUN sleep 50s
RUN ['./consoleAgentManager','configure','nidhi.kalamkar@hughes.com.sit2','reset123']
