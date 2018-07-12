curl -X POST -d '{ "name": "nom" }'  -H 'Content-Type: application/json' http://localhost:5000/api/v1/products

curl -X PATCH -d '{ "name": "AFFREUX" }'  -H 'Content-Type: application/json' http://localhost:5000/api/v1/products
/2
curl -X DELETE    http://localhost:5000/api/v1/products
/3
