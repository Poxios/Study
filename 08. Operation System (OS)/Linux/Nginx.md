```conf

http {
	##
	# Basic Settings
	##

    server {
            server_name 211.37.150.202:443;

            location /api {
                    proxy_pass https://127.0.0.1:3001;
            }
			location /docs {
                    proxy_pass https://127.0.0.1:3001/docs;
            }
			location / {
                    # 이 경우는 바로 static serve
					root   "/home/ubuntu/MWMS_WEB/WEB_APP_MWMS_RackVisor/WEB(FE)/mwms/build";
    				index  index.html index.htm;
    				try_files $uri $uri/ /index.html;
			}

            listen 443 ssl; # managed by Certbot
            ssl_certificate "/home/ubuntu/WEB_APP_MWMS_RackVisor/WEB(BE)/src/cert/certificate.crt"; # managed by Cert>
            ssl_certificate_key "/home/ubuntu/WEB_APP_MWMS_RackVisor/WEB(BE)/src/cert/private.key"; # managed by Ce>

            # include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
            # ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    }

    # 80 포트로 접근시 443 포트로 리다이렉트 시켜주는 설정
    server {
             return 301 https://$host$request_uri;

            listen 80;
            server_name 211.37.150.202;
            return 404; # managed by Certbot
    }
}

```

* Nginx를 이용해서 Reverse Proxy로 하나의 서버 안에서 여러 서버를 돌리고, 외부에서는 안에서 무슨 일이 일어나는지 모르도록 하기.