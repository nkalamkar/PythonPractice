FROM scratch
RUN ubuntu:infa
CMD [cd /opt]
CMD [mkdir ics]
CMD [cd /ics]
CMD [mkdir secureagent]
ADD agent64_inatll.bin /opt/ics/secureagent
CMD [./agent64_install.bin /opt/ics/secureagent]
WORKDIR /opt/ics/secureagent/apps/agentcore
CMD [./infaagent startup]
CMD [./consoleAgentManager nidhi.kalamkar@hughes.com.sit2 reset123]
