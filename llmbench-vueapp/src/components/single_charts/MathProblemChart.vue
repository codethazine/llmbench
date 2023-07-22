<template>
    <div>
      <canvas id="mathProblemChart"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref, toRefs, watch } from 'vue';
  import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
    
  Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  function getMonthName(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString('default', { month: 'long' });
  }

  
  
  export default {
    name: 'MathProblemChart',
    props: ['fromMonth', 'toMonth', 'modelData', 'modelId'],
    setup(props) {
      const { fromMonth, toMonth } = toRefs(props);
      const chart = ref(null);
  
      const createChart = () => {
        if (chart.value) {
          chart.value.destroy(); // Destroy the old chart before creating a new one
        }
        
        chart.value = new Chart(document.getElementById('mathProblemChart'), {
          type: 'bar',
          data: {
            labels: ['Accuracy', 'Verbosity', 'Overlap'],
            datasets: [{
              label: getMonthName(fromMonth.value),
              data: [65, 59, 80],
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }, {
              label: getMonthName(toMonth.value),
              data: [28, 48, 40],
              backgroundColor: 'rgba(153, 102, 255, 0.2)',
              borderColor: 'rgba(153, 102, 255, 1)',
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
        });
      };
  
      onMounted(createChart);
  
      watch([fromMonth, toMonth], createChart); // Recreate the chart when fromMonth or toMonth changes
  
      return { chart };
    }
  }
  </script>  
  