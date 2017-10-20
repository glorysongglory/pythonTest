/**
 * Created by glory on 2017/10/20.
 */
<script>
    $(document).ready(function () {
    var data = {
         data: JSON.stringify({"lesson": "Operation System", "score": 100})
   }
      $.ajax({
        url:"/testJson",
        type: 'POST',
        data: data,
        success: function (msg) {
            alert(msg.name)
        }
    })
  });
</script>
