FROM minimalcompact/thumbor:latest

COPY . /home/plugin

RUN cd /home/plugin && pip install -e ./

ENTRYPOINT ["/docker-entrypoint.sh"]

# running thumbor multiprocess via circus by default
# to override and run thumbor solo, set THUMBOR_NUM_PROCESSES=1 or unset it
CMD ["circus"]

EXPOSE 80 8888
