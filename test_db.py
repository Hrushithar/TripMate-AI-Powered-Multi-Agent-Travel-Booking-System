import psycopg
try:
    psycopg.connect("postgresql://hrushi:pass@dpg-daqgr4qd0e5s73ahhdgg-a.oregon-postgres.render.com/tripmate_database?sslmode=require")
except Exception as e:
    print(e)
