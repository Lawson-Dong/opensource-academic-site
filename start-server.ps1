# 创建一个简单的HTTP服务器
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add('http://localhost:8080/')
$listener.Start()

Write-Host '服务器已启动，访问 http://localhost:8080'

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response
    
    # 获取请求的路径
    $path = $request.Url.LocalPath
    if ($path -eq '/') {
        $path = '/index.html'
    }
    
    # 构建文件路径
    $filePath = Join-Path -Path 'docs' -ChildPath $path.Substring(1)
    
    # 检查文件是否存在
    if (Test-Path $filePath -PathType Leaf) {
        # 读取文件内容
        $content = Get-Content -Path $filePath -Raw
        
        # 设置响应内容类型
        $extension = [System.IO.Path]::GetExtension($filePath)
        switch ($extension) {
            '.html' {
                $response.ContentType = 'text/html'
            }
            '.md' {
                $response.ContentType = 'text/markdown'
            }
            '.js' {
                $response.ContentType = 'application/javascript'
            }
            '.css' {
                $response.ContentType = 'text/css'
            }
            default {
                $response.ContentType = 'application/octet-stream'
            }
        }
        
        # 写入响应内容
        $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
        $response.ContentLength64 = $buffer.Length
        $response.OutputStream.Write($buffer, 0, $buffer.Length)
    } else {
        # 文件不存在
        $response.StatusCode = 404
        $content = '<html><body><h1>404 Not Found</h1></body></html>'
        $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
        $response.ContentLength64 = $buffer.Length
        $response.OutputStream.Write($buffer, 0, $buffer.Length)
    }
    
    $response.Close()
}

# 停止服务器
$listener.Stop()
$listener.Close()