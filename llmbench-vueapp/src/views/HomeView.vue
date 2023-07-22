<template>
  <!-- HEADER -->
  <header class="navbar bg-base-300 mt-auto">
    <div class="flex-1">
      <a href="/" class="btn btn-ghost normal-case text-xl">LLMBench</a>
    </div>
    <div class="flex-none">
      <button class="btn btn-square btn-ghost">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path>
        </svg>
      </button>
    </div>
  </header>

  <!-- HERO SECTION -->
  <div class="hero min-h-screen bg-base-200">
    <div class="text-center hero-content">
      <div class="max-w-md">
        <h1 class="mb-5 text-5xl font-bold">LLMBench</h1> 
        <p class="mb-5">Open and recurrent LLM models benchmarking.</p> 
        <div class="flex justify-center">
          <a href="#bench" class="btn btn-neutral">Check benchamarks</a>
        </div>
      </div>
    </div>
  </div>

  <!-- BENCHMARKS -->
  <!-- FOR EACH MODEL IN MODELS SHOW NAME OF THE MODEL WITH VUE -->
  <div class="min-h-screen" id="bench">
    <div 
      class="card compact bg-base-100" 
      v-for="(item, index) in items" 
      :key="index">
      <div class="card-body">
        <model-benchmark :model-id="item.name" :model-name="item.name" />
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="footer p-10 bg-neutral text-neutral-content mt-auto">
    <div>
      <span class="footer-title">Services</span> 
      <a href="/" class="link link-hover">Branding</a>
      <a href="/" class="link link-hover">Design</a>
      <a href="/" class="link link-hover">Marketing</a>
      <a href="/" class="link link-hover">Advertisement</a>
    </div> 
    <div>
      <span class="footer-title">Company</span> 
      <a href="/" class="link link-hover">About us</a>
      <a href="/" class="link link-hover">Contact</a>
      <a href="/" class="link link-hover">Jobs</a>
      <a href="/" class="link link-hover">Press kit</a>
    </div> 
    <div>
      <span class="footer-title">Legal</span> 
      <a href="/" class="link link-hover">Terms of use</a>
      <a href="/" class="link link-hover">Privacy policy</a>
      <a href="/" class="link link-hover">Cookie policy</a>
    </div>
  </footer>
</template>

<script>
import ModelBenchmark from '@/components/ModelBenchmark.vue';

export default {
  components: {
    ModelBenchmark
  },
  data() {
    return {
      items: [
        { name: "GPT 3.5", description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam necessitatibus incidunt ut officiis explicabo inventore." },
        /*{ name: "GPT 4", description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam necessitatibus incidunt ut officiis explicabo inventore." },
        { name: "Claude 2", description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam necessitatibus incidunt ut officiis explicabo inventore." },*/
      ]
    }
  }
}
</script>
<style scoped>
.navbar, .hero, .card, .footer {
    color: white;
  }
</style>