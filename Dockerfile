FROM python

COPY src/ /opt/backend
COPY start.sh start.sh
CMD ["start.sh"]
EXPOSE 5002