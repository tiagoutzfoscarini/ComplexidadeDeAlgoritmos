###

## Parameters
param(
    [Parameter(Mandatory=$true)]
    [int]$listSize = 10000
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
    return @(QuickSort($left) + $pivot + QuickSort($right))
}


# Função bubble sort
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


## função para gerar lista de 1000 numeros aleatorios inteiros
function GerarLista() {
    $arr = @()
    for ($i = 0; $i -lt 10000; $i++) {
        $arr += Get-Random -Minimum 1 -Maximum 10000
    }
    return $arr
}



## MAIN
$lista = GerarLista

$startTime = Get-Date
$listaOrdenadaBubbleSort = BubbleSort($lista)
$endTime = Get-Date

Write-Host "Tempo de execução BubbleSort: $(($endTime - $startTime).TotalMilliseconds)ms"

$startTime = Get-Date
$listaOrdenadaQuickSort = QuickSort($lista)
$endTime = Get-Date

Write-Host "Tempo de execução QuickSort: $(($endTime - $startTime).TotalMilliseconds)ms"
