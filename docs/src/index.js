
$(document).ready(function () {
    let defaultStore = "Watsons";
    let storeData = changeStore(defaultStore)
    $('#storeName').text(storeData[1]);
    $('#ajaxTable').dataTable({
        ajax: {
            url: storeData[0],
            dataSrc: "",
            processData: false,
        },
        columns: [
            {data: "RetrieveTime"},
            {data: "Store"},
            {data: "Title"},
            {data: "Price"},
            {
                data: "URL",
                render: function (data, type, full, meta) {
                    return '<a class= "btn btn-outline-primary" href=' + data + ' role="button">Click me</a>';
                }
            }]
    });
})

function changeHandler(name) {
    let storeData = changeStore(name)
    $('#ajaxTable').DataTable().clear() //must need
    $('#ajaxTable').DataTable().ajax.url(storeData[0]).load();//must need
    $('#ajaxTable').DataTable().ajax.reload()//must need
    $('#storeName').text(storeData[1]);

}

function changeStore(name){
    let storeData = [];
    switch (name) {
        case "HKTVMall":
            storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/HKTVMall.json';
            storeData[1] = "HKTVMall";
            break;
        case "Watsons":
            storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/watsons.json';
            storeData[1] = "Watsons";
            break;
        case "Amazon":
            storeData[0] = 'json/amazon.json';
            storeData[1] = "Amazon";
            break;
    }
    return storeData;
}