for id in `docker container ls | grep postgres | awk '{ print $1 }'`;
do 
	docker container stop $id
done

docker container prune --force
