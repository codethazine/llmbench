<template>
    <div>
      <canvas id="mathProblemChart"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
  
  Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  export default {
    name: 'MathProblemChart',
    props: ['fromMonth', 'toMonth'],
    setup() {
      const chart = ref(null);
      
      onMounted(() => {
        chart.value = new Chart(document.getElementById('mathProblemChart'), {
          type: 'bar',
          data: {
            labels: ['Accuracy', 'Verbosity', 'Overlap'],
            datasets: [{
              label: 'March 2023',
              data: [65, 59, 80],
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }, {
              label: 'June 2023',
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
      });
  
      return { chart };
    }
  }
  </script>
  