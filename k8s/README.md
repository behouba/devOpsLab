## Environment
- Linux Ubuntu LTS 22.04 Jammy jelly fish
- AMD ryzen 5 5600H

# Lab 9

## Output of `kubectl get pods,svc`

```bash
$ kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/devops-labs-5f58bb6654-7f2rr   1/1     Running   0          12m

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/devops-labs   LoadBalancer   10.106.220.144   <pending>     5000:30968/TCP   11m
service/kubernetes    ClusterIP      10.96.0.1        <none>        443/TCP          26m

```

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.1.png)



## Output of `minikube service --all`

```bash
$ minikube service --all
|-----------|------|-------------|-----------------------------|
| NAMESPACE | NAME | TARGET PORT |             URL             |
|-----------|------|-------------|-----------------------------|
| default   | app  |        5000 | http://192.168.59.100:31591 |
|-----------|------|-------------|-----------------------------|
|-----------|---------------------------|-------------|-----------------------------|
| NAMESPACE |           NAME            | TARGET PORT |             URL             |
|-----------|---------------------------|-------------|-----------------------------|
| default   | devops-lab-app-deployment |        5000 | http://192.168.59.100:32345 |
|-----------|---------------------------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app in default browser...
🎉  Opening service default/devops-lab-app-deployment in default browser...
```

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.3.png)


## Browser screenshot

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab9_submission/k8s/images/lab9.2.png)

# Lab 10

## Helm install

```bash
$ helm install app-python app-python-0.1.0.tgz 
NAME: app-python
LAST DEPLOYED: Tue Jun 28 02:40:48 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

## Output of `kubectl get pods,svc`
```bash
$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-98cc49b8d-4t75w   0/1     Running   0          4s
pod/app-python-98cc49b8d-g9wzt   0/1     Running   0          4s
pod/app-python-98cc49b8d-zlw2b   0/1     Running   0          4s

NAME                                TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python                  NodePort       10.101.156.166   <none>        5000:30141/TCP   4s
service/devops-lab-app-deployment   LoadBalancer   10.108.235.102   <pending>     5000:32345/TCP   143m
service/kubernetes                  ClusterIP      10.96.0.1        <none>        443/TCP          3h41m

```

## Screenshots

![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab10_submission/k8s/images/lab10.1.png)


![Screenshoot](https://raw.githubusercontent.com/behouba/devOpsLab/lab10_submission/k8s/images/lab10.2.png)
