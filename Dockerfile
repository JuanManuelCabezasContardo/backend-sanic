FROM python

COPY src/ /opt/backend

CMD ["start.sh"]
EXPOSE 5002