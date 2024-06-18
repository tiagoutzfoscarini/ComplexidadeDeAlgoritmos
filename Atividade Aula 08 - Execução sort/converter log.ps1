###
# converter para facilitar a geração de gráficos

$caminho = "C:\Users\Tiago\GitHub\ComplexidadeDeAlgoritmos\Atividade Aula 08 - Execução sort\execlog\execlog-fit-23725\tempos.csv"

$content = Get-Content $caminho

$output = @()

foreach ($c in $content) {
    Write-Progress -Id 1 -Activity "Processing" -Status "Processing $c" -PercentComplete (($content.IndexOf($c) / $content.Count) * 100)

    $c = $c -split ';'

    # Sample item:
    $item = [PSCustomObject]@{
        iteration = -1
        quicksort = -1
        mergeSort= -1
        heapSort = -1
        countingSort = -1
        radixSort = -1
        bucketSort = -1
    }

    if ($null -eq ($output | Where-Object {$_.iteration -eq $c[1]})) {
        $item.iteration = $c[1]
        $item.$($c[0]) = $c[2]
        $output += $item
    } else {
        $output | Where-Object {$_.iteration -eq $c[1]} | ForEach-Object {
            $_.$($c[0]) = $c[2]
        }
    
    }
}
Write-Progress -Id 1 -Activity "Processing" -Status "Processing" -Completed


$output | Export-Csv ".\execlog\execlog-fit-23725\tempos-converted.csv" -NoTypeInformation
