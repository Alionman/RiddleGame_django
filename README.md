# RiddleGame_django
这个项目是我接的商场活动，主要是一个猜灯谜的H5小应用；
域名：www.alionman.xin
配置：阿里云centos cpu:1核 内存:2GB 带宽:1Mbps 
服务器部署：Apache
服务端：django+mysql+wsgi
前端vue.js
实现功能：
1.链接点击次数统计
2.答题页面互动，将手机号码及分数提交服务端
3.提交后不允许再次答题
4.从数据库中随机抽取三个号码显示在抽奖页面(/luckydraw)

总结:
前端文件部署到服务器后一定要递归chmod赋予权限，不然通过域名无法访问；
