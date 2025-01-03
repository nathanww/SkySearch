$files = Get-ChildItem -Path . -Filter newjersey2*.txt
$outfile = "mergednj.txt"

foreach ($file in $files) {
    Add-Content -Path $outfile -Value "=== $($file.Name) ==="
    Get-Content -Path $file.FullName | Add-Content -Path $outfile 
}
