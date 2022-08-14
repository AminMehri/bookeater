FROM nginx:latest

# COPY cert.pem /etc/ssl/certs/cert.pem
# COPY key.pem /etc/ssl/private/key.pem
COPY nginx.conf /etc/nginx/conf.d/default.conf

#-----
# RUN mkdir /frontend
# COPY ./dist /frontend
#-----

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
