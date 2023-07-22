<template>
    <div>
      <canvas id="visualReasoningChart"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
  
  Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  export default {
    name: 'VisualReasoningChart',
    props: ['fromMonth', 'toMonth'],
    setup() {
      const chart = ref(null);
      
      onMounted(() => {
        chart.value = new Chart(document.getElementById('visualReasoningChart'), {
          type: 'bar',
          data: {
            labels: ['Exact Match', 'Verbosity', 'Overlap'],
            datasets: [{
              label: 'March 2023',
              data: [50, 69, 75],
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1
            }, {
              label: 'June 2023',
              data: [38, 48, 55],
              backgroundColor: 'rgba(255, 159, 64, 0.2)',
              borderColor: 'rgba(255, 159, 64, 1)',
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
      });
  
      return { chart };
    }
  }
  </script>
  