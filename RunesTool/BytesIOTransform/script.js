document.getElementById("imageForm").addEventListener("submit", function(event) {
    event.preventDefault(); // 防止表單提交的默認行為

    var inputData = document.getElementById("inputData").value;

    // 檢查輸入的二進制數據格式
    if (!inputData.startsWith("\\x")) {
        alert("請輸入有效的二進制編碼，例如：\x89\x50\x4e\x47...");
        return;
    }

    // 將用戶輸入的內容轉換為二進制數據
    var byteArray = [];
    var hexRegex = /\\x([0-9A-Fa-f]{2})/g; // 匹配十六進制格式的部分
    var result;

    // 解析輸入的二進制字符串並轉換
    while ((result = hexRegex.exec(inputData)) !== null) {
        byteArray.push(parseInt(result[1], 16));
    }

    // 創建 Uint8Array 以轉換為圖像
    var imageData = new Uint8Array(byteArray);
    var blob = new Blob([imageData], { type: 'image/png' });
    var imgUrl = URL.createObjectURL(blob);

    // 顯示生成的圖片
    var img = new Image();
    img.src = imgUrl;
    img.onload = function() {
        var canvas = document.getElementById("outputCanvas");
        var context = canvas.getContext("2d");
        canvas.width = Math.min(img.width, 512); // 限制canvas的最大寬度
        canvas.height = Math.min(img.height, 512); // 限制canvas的最大高度
        context.drawImage(img, 0, 0); // 將圖像繪製到 canvas 上
    };
});

document.getElementById("downloadBtn").addEventListener("click", function() {
    var canvas = document.getElementById("outputCanvas");
    var link = document.createElement("a");
    link.download = "generated_image.png";
    link.href = canvas.toDataURL(); // 將 canvas 轉換為圖片的 URL
    link.click(); // 自動觸發下載
});

// 處理文件上傳和轉換為二進制
document.getElementById("convertBtn").addEventListener("click", function(event) {
    var fileInput = document.getElementById("fileInput");
    var outputArea = document.getElementById("binaryOutput");

    // 確保有選擇文件
    if (fileInput.files.length === 0) {
        alert("請選擇一個圖像文件。");
        return;
    }

    var file = fileInput.files[0];
    var reader = new FileReader();

    // 當檔案讀取完成後，將二進制數據顯示在文本區域
    reader.onload = function(e) {
        var arrayBuffer = e.target.result;
        var uint8Array = new Uint8Array(arrayBuffer);
        
        // 將 ArrayBuffer 轉換為十六進制字符串
        var binaryString = "";
        for (var i = 0; i < uint8Array.length; i++) {
            binaryString += '\\x' + uint8Array[i].toString(16).padStart(2, '0'); // 將數字轉為十六進制並補零
        }
        
        outputArea.value = binaryString; // 將二進制數據顯示在 textarea 中
    };

    // 讀取圖像檔案為 ArrayBuffer
    reader.readAsArrayBuffer(file);
});