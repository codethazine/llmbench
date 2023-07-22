<script>
    import { onMount, reactive } from 'svelte';
    import { Bar } from 'chart.js';
    import { Button } from "daisyui";

    let modelId;
    let modelName;
    let selectedAction = 'Drift';
    let selectedBenchmark = 'Solving Math Problems';
    let fromMonth = 'March 2023';
    let toMonth = 'June 2023';
    
    const benchmarks = ['Solving Math Problems', 'Answering Sensitive Questions', 'Code Generation', 'Visual Reasoning'];
    
    let chartData = reactive({
        labels: [fromMonth, toMonth],
        datasets: [
            {
                label: 'Metric 1',
                data: [Math.random() * 100, Math.random() * 100],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            },
            {
                label: 'Metric 2',
                data: [Math.random() * 100, Math.random() * 100],
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            },
            {
                label: 'Overlap',
                data: [Math.random() * 100, Math.random() * 100],
                backgroundColor: 'rgba(255, 159, 64, 0.2)',
                borderColor: 'rgba(255, 159, 64, 1)',
                borderWidth: 1
            }
        ]
    });

    onMount(() => {
        updateChartData();
    });

    function updateChartData() {
        switch (selectedBenchmark) {
            case 'Solving Math Problems':
                chartData.datasets[0].label = 'Accuracy';
                chartData.datasets[1].label = 'Verbosity';
                break;
            case 'Answering Sensitive Questions':
                chartData.datasets[0].label = 'Answer Rate';
                chartData.datasets[1].label = 'Verbosity';
                break;
            case 'Code Generation':
                chartData.datasets[0].label = 'Directly Executable';
                chartData.datasets[1].label = 'Verbosity';
                break;
            case 'Visual Reasoning':
                chartData.datasets[0].label = 'Exact Match';
                chartData.datasets[1].label = 'Verbosity';
                break;
            default:
                break;
        }
        
        chartData.datasets[0].data = [Math.random() * 100, Math.random() * 100];
        chartData.datasets[1].data = [Math.random() * 100, Math.random() * 100];
        chartData.datasets[2].data = [Math.random() * 100, Math.random() * 100];
    }
</script>

<div class="min-h-screen">
    <h1>{modelName}</h1>
    <Button disabled>{selectedAction}</Button>
    <Button disabled coming soon>Performance</Button>
    <Button disabled coming soon>Speed</Button>

    <div>
        <select bind:value={selectedBenchmark} on:change={updateChartData}>
            {#each benchmarks as benchmark}
                <option>{benchmark}</option>
            {/each}
        </select>
        <span>From: {fromMonth}</span>
        <span>To: {toMonth}</span>
    </div>

    <div>
        <bar {chartData} options={{ responsive: true }}/>
    </div>
</div>
