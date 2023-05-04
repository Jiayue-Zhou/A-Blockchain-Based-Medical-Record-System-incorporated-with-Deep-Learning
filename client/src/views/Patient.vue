<template>
  <div>
    <div class="big_screen">
    <div class="input_area">
      <div v-for="feature in features" :key="feature">
        <label>{{ feature }}</label>
        <div class="sub_area">
          <input v-model="input_values[feature]" type="text" placeholder="Please enter">
        </div>
        </div>
      <a href="javascript:;" class="button1" @click="onsubmit();">Submit</a>
      </div>
      <div class="drag_upload">
        <input type="file" accept=".csv" id = "fileInputCSV" @change="handleChange()"/>
      </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import detectEthereumProvider from '@metamask/detect-provider';
import Papa from 'papaparse';

export default {
  name: 'Patient',
  data() {
    return {
      features: [
        'Age',
        'Gender',
        'Air Pollution',
        'Alcohol use',
        'Dust Allergy',
        'OccuPational Hazards',
        'Genetic Risk',
        'chronic Lung Disease',
        'Balanced Diet',
        'Obesity',
        'Smoking',
        'Passive Smoker',
        'Chest Pain',
        'Coughing of Blood',
        'Fatigue',
        'Weight Loss',
        'Shortness of Breath',
        'Wheezing',
        'Swallowing Difficulty',
        'Clubbing of Finger Nails',
        'Frequent Cold',
        'Dry Cough',
        'Snoring',
      ],
      input_values: {},
    };
  },
  methods: {
    predict(val) {
      const path = 'http://localhost:5000/patient';
      axios.post(path, val)
        .then((response) => {
          console.log('Submit Success.');
          const message = `Our AI suggests your possibility of getting lung cancer is

                                  ${response.data.answer}.`;
          alert(message);
          console.log(response.data.answer);
        });
    },
    handleChange() {
      const fileInput = document.getElementById('fileInputCSV');
      this.importfxx(fileInput);
    },
    importfxx(obj) {
      console.log(obj);
      let dp;
      Papa.parse(obj.files[0], {
        header: true,
        complete(results) {
          console.log(results);
          dp = results.data;
        },
      });
      setTimeout(() => {
        this.backInput(dp);
      }, 1500);
    },
    backInput(dp) {
      console.log(dp);
      this.features.forEach((feature) => {
        this.$set(this.input_values, feature, dp[0][feature]);
      });
    },
    onsubmit() {
      const data = {
        ...this.input_values,
      };
      this.predict(data);
    },
  },
  async mounted() {
    const provider = await detectEthereumProvider();
    if (provider === window.ethereum) {
      window.ethereum.enable().then(() => {
      });
    } else {
      console.log(provider);
      alert('Please use MetaMask');
    }
  },
};
</script>

<style scoped>

.input_area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.sub_area {
  margin-bottom: 0.5em;
}
.big_screen {
  display: flex;
  justify-content: center;
}
.drag_upload {
  display:inline-block;
  margin-top: 2em;
  margin-left: 2em;
}
</style>
