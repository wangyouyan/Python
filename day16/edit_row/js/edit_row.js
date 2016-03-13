function CheckAll(mode,tb) {
    //1、选中checkbox
    //2、如果已经进入编辑模式，让选中行进入编辑模式状态
    //tb = #tb1
    //$(tb) = $('#tb1')
    $(tb).children().each(function(){
        //$(this) 表示循环过程中，每一个tr,每一行数据
        var tr = $(this);
        var isChecked
    })
}

function CheckReverse(mode,tb) {

}

function CheckCancel(mode,tb) {
    //1、取消选中checkbox
    //2、如果已经进入编辑模式，行推出编辑状态
    $(tb).children().each(function(){
        var tr = $(this);
        if(tr.find(':checkbox').prop('checked')){
            //移除选中
            tr.find(':checkbox').prop('checked',false);
        var isEditing = $mode.hasClass('editing');
        if(isEditing == true) {
            //当前行，推出编辑状态
            tr.children().each(function){
                var td = $(this);
                if(td.attr('edit') == 'true') {
                    var inp = td.children(':first');
                    var input_value = inp.val();
                    td.text(input_value);
                }
            });
        }
        }
    });
}

function EditMode(ths,tb) {
    var isEditing = $(ths).hasClass('editing');
    if(isEditing){
        //退出编辑模式
        $(ths).text('进入编辑模式');
        $(ths).removeClass('editing');
        $(tb).children().each(function(){
            var tr = $(this);
            if(tr.find(':checkbox').prop('checked')){
                //当前行，退出编辑模式
                tr.children().each(function(){
                    var td = $(this);
                    if(td.attr('edit')) == 'true'){
                        var inp == td.children(':first');
                        var input_value = inp.val();
                    }
                });
            }
        });
    }else{
        //进入编辑模式
        $(ths).text('退出编辑模式');
        $(ths).addClass('editing');
        $(tb).children().each(function(){
            //$(this) 表示循环过程中，每一个tr,每一行数据
            var tr = $(this);
            var isChecked = $(this).find(':checkbox').prop('checked');
            if(isChecked==true){
                //当前行进入编辑状态
                tr.children().each(function(){
                    var td = $(this);
                    if(td.attr('edit') == 'true'){
                        var text = td.text();
                        var temp = "<input type='text' value='" + text+ "'/>"
                        td.html(temp)
                    }
                });
            }
        });
    }
}









