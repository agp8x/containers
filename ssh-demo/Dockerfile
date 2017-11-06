FROM alpine:3.6
RUN apk add --update --no-cache python3 py3-numpy openssh-server
RUN pip3 install IPython
RUN ssh-keygen -A && \
	adduser -D -s "/init.py" demo && \
	passwd -u demo
COPY ["init.py", "/init.py"]
EXPOSE 22
RUN echo "PermitEmptyPasswords yes" >> /etc/ssh/sshd_config && \
	echo "PrintMotd no" >> /etc/ssh/sshd_config
CMD ["/usr/sbin/sshd", "-D", "-e"]