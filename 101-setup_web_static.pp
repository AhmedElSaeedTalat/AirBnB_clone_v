# script to set up nginx
node default {
    exec {'set up nginx':
        command  => 'sudo apt-get -y update;
        sudo apt-get install -y nginx;
        sudo mkdir -p /data/;
        sudo mkdir -p /data/web_static/;
        sudo mkdir -p /data/web_static/releases/;
        sudo mkdir -p /data/web_static/shared/;
        sudo mkdir -p /data/web_static/releases/test/;
        content="<html>
          <head>
          </head>
          <body>
            Holberton School
          </body>
        </html>"
        echo "$content" | sudo tee /data/web_static/releases/test/index.html;
        sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
        sudo chown -R ubuntu:ubuntu /data/;
        to_replace="# pass PHP scripts to FastCGI server";
        replace_with="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}";
        sudo sed -i "s|$to_replace|$replace_with|g" /etc/nginx/sites-available/default;
        sudo service nginx restart',
        provider => shell
    }
}
