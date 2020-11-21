docker build -t rtikes/multi-client:latest -t rtikes/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t rtikes/multi-server:latest -t rtikes/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t rtikes/multi-worker:latest -t rtikes/multi-worker:$SHA -f ./worker/Dockerfile ./worker

docker push rtikes/multi-client:latest
docker push rtikes/multi-server:latest
docker push rtikes/muli-worker:latest

docker push rtikes/multi-client:$SHA
docker push rtikes/multi-server:$SHA
docker push rtikes/muli-worker:$SHA

kubectl apply -f k8s
kubectl set image deployments/server-deployment server=rtikes/multi-server:$SHA
kubectl set image deployments/client-deployment client=rtikes/multi-client:$SHA
kubectl set image deployments/worker-deployment worker=rtikes/multi-worker:$SHA