###

## Parameters
param(
    [Parameter(Mandatory=$true)]
    [int]$listSize = 1000
)


## Functions
# função quick sort
function QuickSort($arr) {
    if ($arr.Length -le 1) {
        return $arr
    }

    $pivot = $arr[0]
    $left = @()
    $right = @()

    for ($i = 1; $i -lt $arr.Length; $i++) {
        if ($arr[$i] -lt $pivot) {
            $left += $arr[$i]
        } else {
            $right += $arr[$i]
        }
    }

    return @(QuickSort($left)) + $pivot + @(QuickSort($right))
}


# função bubble sort
function BubbleSort($arr) {
    $n = $arr.Length
    for ($i = 0; $i -lt $n; $i++) {
        for ($j = 0; $j -lt $n - $i - 1; $j++) {
            if ($arr[$j] -gt $arr[$j + 1]) {
                $temp = $arr[$j]
                $arr[$j] = $arr[$j + 1]
                $arr[$j + 1] = $temp
            }
        }
    }
    return $arr
}


## função para gerar lista de $listSize numeros aleatorios inteiros
function GerarLista($size) {
    $arr = @()
    for ($i = 0; $i -lt $size; $i++) {
        $arr += Get-Random -Minimum 1 -Maximum $size
    }
    return $arr
}


## MAIN
$lista = GerarLista($listSize)

$listaOrdenadaBubbleSort = $lista.Clone()
$listaOrdenadaQuickSort = $lista.Clone()

#
Write-Host "Executando BubbleSort para lista de $listSize elementos..."

$startTime = Get-Date
$listaOrdenadaBubbleSort = BubbleSort($listaOrdenadaBubbleSort)
$endTime = Get-Date

Write-Host "Tempo de execução BubbleSort: $(($endTime - $startTime).TotalMilliseconds)ms" -ForegroundColor Green

# 
Write-Host "Executando QuickSort para lista de $listSize elementos..."

$startTime = Get-Date
$listaOrdenadaQuickSort = QuickSort($listaOrdenadaQuickSort)
$endTime = Get-Date

Write-Host "Tempo de execução QuickSort: $(($endTime - $startTime).TotalMilliseconds)ms" -ForegroundColor Green


# Check (se retornar algo a lista está diferente)
Compare-Object $listaOrdenadaBubbleSort $listaOrdenadaQuickSort -SyncWindow 0

Compare-Object ($lista | Sort) $listaOrdenadaQuickSort  -SyncWindow 0

Compare-Object ($lista | Sort) $listaOrdenadaBubbleSort  -SyncWindow 0
