<script>
    $(document).ready(function () {
        var student = new Object();
        student.name = "Peng Shuang";
        student.age = 23;
        student.location = "China";
        var data = JSON.stringify(student)

    $.ajax({
        url: "/sendjson2",
        type: "POST",
        data: data,
        success: function (msg) {
            alert(msg.time)
        }
    })
    })
</script>