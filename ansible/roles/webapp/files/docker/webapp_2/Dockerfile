FROM ubuntu:19.10

# Install nginx webserver
RUN apt update && apt-get install --no-install-recommends -y \
nginx && \
apt-get clean -y && \
rm -rf /var/lib/apt/lists/*

# Copy nginx index file
COPY index.htm /var/www/html/index.htm

EXPOSE 8082

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
