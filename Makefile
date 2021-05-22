build_admin: admin
	cd ./admin/ && yarn && yarn build

clean: admin/dist
	rm -rf admin/dist