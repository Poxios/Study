```conf

http {
	##
	# Basic Settings
	##

    server {
            server_name EXTERNAL_IP_HERE:443;

             location /api {
					if ($request_method = OPTIONS ) {
						return 204;
					}

                    # 개발용으로 다 허용할 때 사용하는 옵션. 보통 때는 꺼야 함.
    				proxy_hide_header Access-Control-Allow-Origin; # 이거 해야 로컬 백엔드에서 달고오는 헤더를 숨기고 새로 작성 가능.
    				add_header 'Access-Control-Allow-Origin' '*'; # ONLY FOR DEV ENV
			        add_header 'Access-Control-Allow-Credentials' 'true'; # ONLY FOR DEV ENV
        			add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, DELETE, PUT'; # ONLY FOR DEV ENV
        			add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type'; # ONLY FOR DEV ENV
					# 위 헤더 중에 하나라도 빠지면 작동 안 함.

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