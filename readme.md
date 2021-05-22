# News-CMS

Tool to manage news supplied to VA

## How to start development

1. Start mongodb
   ```shell
   docker-compose up -d mongodb
   ```
1. Build admin dashboard
   ```shell
   git submodule update --init
   make build_admin
   ```
1. Start the API
   ```shell
   python main.py
   ```

Then:

- Access http://localhost:8000 for the API
- Access http://localhost:8000/admin/ for the admin dashboard

## How to deploy