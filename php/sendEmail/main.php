<? 

require_once('emailclass.php');

//发送邮件

//內容 www.jbxue.com
$message = 
"<tbody><tr>
<td style='padding: 30px 67.5pt; border-color: rgb(102, 102, 102); border-width: 1px; border-style: solid;'>
<table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' style='border-collapse: collapse;'>
 <tbody><tr>
  <td style='padding: 0px 0cm 15pt;'>
  <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left;'><b><span style='font-size: 20px; font-family: SimSun; color: rgb(213, 213, 213);'>BOSS</span></b><b><span style='font-size: 20px; font-family: SimSun; color: rgb(213, 213, 213);'>直聘 <span></span></span></b></p>
  </td>
 </tr>
 <tr>
  <td style='border-top: none; border-right: none; border-bottom: none; border-image: initial; border-left: 4px solid rgb(98, 213, 200); background: white; padding: 22px 0cm 19.5pt 6pt;'>
  <table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' style='width: 600px; border-collapse: collapse;'>
   <tbody><tr>
    <td style='padding: 0px 0cm 0cm 15pt;'>
    <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left;'><b><span style='font-family: SimSun; color: black;'>Hi, </span></b><b><span style='font-family: SimSun; color: black;'>梁露<span></span></span></b></p>
    </td>
   </tr>
   <tr>
    <td style='padding: 10px 0cm 0cm 15pt;'>
    <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left; line-height: 14px;'><span style='font-family: Arial, sans-serif; color: black;'>BOSS</span><span style='font-family: SimSun; color: black;'>直聘上与你沟通</span><span style='font-family: Arial, sans-serif; color: black;'> </span><span style='font-family: Arial, sans-serif; color: rgb(83, 202, 195);'>CMS </span><span style='font-family: SimSun; color: rgb(83, 202, 195);'>产品经理（</span><span style='font-family: Arial, sans-serif; color: rgb(83, 202, 195);'>onsite Unilever</span><span style='font-family: SimSun; color: rgb(83, 202, 195);'>）</span><span style='font-family: Arial, sans-serif; color: rgb(83, 202, 195);'> | </span><span style='font-family: SimSun; color: rgb(83, 202, 195);'>上海</span><span style='font-family: Arial, sans-serif; color: rgb(83, 202, 195);'>
    10-12K</span><span style='font-family: Arial, sans-serif; color: black;'> </span><span style='font-family: SimSun; color: black;'>职位的候选人给你发了一封简历。</span><span style='font-family: Arial, sans-serif; color: black;'> <span></span></span></p>
    </td>
   </tr>
   <tr>
    <td style='padding: 27px 0cm 0cm;'>
    <table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' style='width: 415px; margin-left: 20px; background: white; border-collapse: collapse;'>
     <tbody><tr>
      <td width='1' style='border-top: 1px solid rgb(215, 215, 215); border-bottom: 1px solid rgb(215, 215, 215); border-left: 1px solid rgb(215, 215, 215); border-image: initial; border-right: none; padding: 14px 0cm 10.5pt 10.5pt;'></td>
      <td style='border-top: 1px solid rgb(215, 215, 215); border-right: 1px solid rgb(215, 215, 215); border-bottom: 1px solid rgb(215, 215, 215); border-image: initial; border-left: none; padding: 10px 7.5pt 7.5pt 0cm;'>
      <table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' style='width: 100%; border-collapse: collapse;'>
       <tbody><tr>
        <td style='padding: 0px;'>
        <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left; line-height: 17px;'><span style='font-family: SimSun; color: black;'><a href='http://sctrack.sc.gg/track/click/eyJtYWlsbGlzdF9pZCI6IDAsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNTY1MjIxOTcxMTY4XzM1MjUzXzI0NzkyXzkxODguc2MtMTBfOV8xM18yMTMtaW5ib3VuZDAka29yaW5hLmxpYW5nQGF1Z21lbnR1bS5jb20iLCAic2lnbiI6ICJhOWM2YmUyYmUyZjI5ZDg3YTVhNjNmY2U1ZTlmOTBlYiIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL20uemhpcGluLmNvbS9yZXN1bWUvcHJldmlldzRtYWlsLzk1MWM3YWYyMjE5MzE2ZTgxbnh5MzltMUVsTlQzNGk3VXZLYlJ1R2tndkRUTUJGbTM2VSU3RSUzRnNpZCUzRG1haWxfcmVzdW1lX25pdSIsICJ1c2VyX2lkIjogMzUyNTMsICJjYXRlZ29yeV9pZCI6IDg4NjQ4fQ==.html' target='_blank' style='color: rgb(0, 0, 255); text-decoration: underline solid rgb(0, 0, 255);'><span style='color: rgb(102, 102, 102); text-decoration: none;'>宗依晴</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>女</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>25</span><span style='color: rgb(153, 153, 153); text-decoration: none;'>岁</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>上海</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>本科</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>3</span><span style='color: rgb(153, 153, 153); text-decoration: none;'>年</span><span style='color: rgb(102, 102, 102); text-decoration: none;'> </span></a></span></p>
        </td>
        <td style='padding: 0px;'>
        <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left;'><span style='font-family: SimSun; color: black;'><a href='http://sctrack.sc.gg/track/click/eyJtYWlsbGlzdF9pZCI6IDAsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNTY1MjIxOTcxMTY4XzM1MjUzXzI0NzkyXzkxODguc2MtMTBfOV8xM18yMTMtaW5ib3VuZDAka29yaW5hLmxpYW5nQGF1Z21lbnR1bS5jb20iLCAic2lnbiI6ICJhOWM2YmUyYmUyZjI5ZDg3YTVhNjNmY2U1ZTlmOTBlYiIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL20uemhpcGluLmNvbS9yZXN1bWUvcHJldmlldzRtYWlsLzk1MWM3YWYyMjE5MzE2ZTgxbnh5MzltMUVsTlQzNGk3VXZLYlJ1R2tndkRUTUJGbTM2VSU3RSUzRnNpZCUzRG1haWxfcmVzdW1lX25pdSIsICJ1c2VyX2lkIjogMzUyNTMsICJjYXRlZ29yeV9pZCI6IDg4NjQ4fQ==.html' target='_blank' style='color: rgb(0, 0, 255); text-decoration: underline solid rgb(0, 0, 255);'><span style='color: rgb(102, 102, 102); text-decoration: none;'>10-15K </span></a></span></p>
        </td>
       </tr>
       <tr>
        <td colspan='2' style='padding: 5px 0cm 0cm;'>
        <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left; line-height: 17px;'><span style='font-family: SimSun; color: rgb(153, 153, 153);'><a href='http://sctrack.sc.gg/track/click/eyJtYWlsbGlzdF9pZCI6IDAsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNTY1MjIxOTcxMTY4XzM1MjUzXzI0NzkyXzkxODguc2MtMTBfOV8xM18yMTMtaW5ib3VuZDAka29yaW5hLmxpYW5nQGF1Z21lbnR1bS5jb20iLCAic2lnbiI6ICJhOWM2YmUyYmUyZjI5ZDg3YTVhNjNmY2U1ZTlmOTBlYiIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL20uemhpcGluLmNvbS9yZXN1bWUvcHJldmlldzRtYWlsLzk1MWM3YWYyMjE5MzE2ZTgxbnh5MzltMUVsTlQzNGk3VXZLYlJ1R2tndkRUTUJGbTM2VSU3RSUzRnNpZCUzRG1haWxfcmVzdW1lX25pdSIsICJ1c2VyX2lkIjogMzUyNTMsICJjYXRlZ29yeV9pZCI6IDg4NjQ4fQ==.html' target='_blank' style='color: rgb(0, 0, 255); text-decoration: underline solid rgb(0, 0, 255);'><span style='color: rgb(153, 153, 153); text-decoration: none;'>旺旺集团</span><span style='color: rgb(153, 153, 153); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>·</span><span style='color: rgb(153, 153, 153); text-decoration: none;'> </span><span style='color: rgb(153, 153, 153); text-decoration: none;'>产品经理</span><span style='color: rgb(153, 153, 153); text-decoration: none;'> </span></a></span></p>
        </td>
       </tr>
      </tbody></table>
      </td>
     </tr>
    </tbody></table>
    </td>
   </tr>
  </tbody></table>
  </td>
 </tr>
 <tr>
  <td style='padding: 10px 0cm 0cm;'>
  <table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' style='border-collapse: collapse;'>
   <tbody><tr>
    <td style='padding: 1px;'>
    <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left; line-height: 18px;'><span style='font-size: 13px; font-family: SimSun; color: rgb(187, 187, 187);'>感谢您使用 BOSS 直聘，如有疑问或建议，请登录 BOSS 直聘企业版，通过在线客服与我们联系。
    <span></span></span></p>
    </td>
   </tr>
   <tr>
    <td style='padding: 1px;'>
    <p class='MsoNormal' style='margin: 0px 0px 0.000133333px; font-size: 14px; font-family: DengXian; text-align: left; line-height: 18px;'><span style='font-size: 13px; font-family: SimSun; color: rgb(187, 187, 187);'>如不想再收到此类邮件，请
    <a href='http://sctrack.sc.gg/track/unsubscribe.do?p=eyJ1c2VyX2lkIjogMzUyNTMsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNTY1MjIxOTcxMTY4XzM1MjUzXzI0NzkyXzkxODguc2MtMTBfOV8xM18yMTMtaW5ib3VuZDAka29yaW5hLmxpYW5nQGF1Z21lbnR1bS5jb20iLCAic2lnbiI6ICI3ZTI5NzI3Y2YwNjMzYzk0YjNkYzFhZmQ5YTU2NDdhNSIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgInJlY2VpdmVyIjogImtvcmluYS5saWFuZ0BhdWdtZW50dW0uY29tIiwgIm1haWxsaXN0X2lkIjogMCwgImNhdGVnb3J5X2lkIjogODg2NDh9' style='color: rgb(0, 0, 255); text-decoration: underline solid rgb(0, 0, 255);'><span style='color: rgb(153, 153, 153);'>点击此处</span></a> 取消订阅
    <span></span></span></p>
    </td>
   </tr>
  </tbody></table>
  </td>
 </tr>
</tbody></table>
</td>
</tr></tbody>";
// 使用mail()函数发送邮件，就必须要有一台不需要验证的SMTP服务器

 //主題 
 $subject = "宗依晴 | 3年，应聘 CMS 产品经理（onsite Unilever） | 上海10-12K【Boss直聘】";
 $subject = "=?UTF-8?B?".base64_encode($subject)."?=";

//收件人 
$sendto = 'fqyd_kz@aliyun.com';

//發件人 
// 
$replyto = 'klein.zhou@augmentum.com.cn';

//附件 
$filename =  iconv('utf-8','gb2312//IGNORE','D:/【CMS 产品经理（onsite Unilever）  上海10-12K】宗依晴 3年.pdf');
$downfilename = '【CMS 产品经理（onsite Unilever）  上海10-12K】宗依晴 3年.pdf';

//附件類別 
$mimetype = "application/pdf";

$mailfile = new CMailFile($subject,$sendto,$replyto,$message,$filename,$downfilename,$mimetype); 
$mailfile->sendfile(); 
?>