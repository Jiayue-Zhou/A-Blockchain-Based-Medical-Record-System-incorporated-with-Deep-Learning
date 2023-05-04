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
        <div class="result_area">
        <label>Doctor Diagnosis Result</label>
        </div>
        <input v-model="test_result" placeholder="Please enter" >
        <a href="javascript:" class="button2" @click="submitForUpload();">Upload the
          patient data</a>
        <div class="result_area">
          <label>Query a patient by Private Password</label>
        </div>
        <input v-model="p_index" placeholder="Please enter" >
        <a href="javascript:" class="button3" @click="submitForQuery();">Submit for the query</a>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import detectEthereumProvider from '@metamask/detect-provider';
import Papa from 'papaparse';
// eslint-disable-next-line import/no-cycle
import router from '../router';

export default {
  name: 'Doctor',
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
          const message = `Our AI predicts your result is ${response.data.answer}.`;
          alert(message);
          console.log(response.data.answer);
        });
    },
    query(val) {
      const path = 'http://localhost:5000/query';
      axios.post(path, val)
        .then((response) => {
          this.queryBack(response.data.answer);
          console.log(response.data.answer);
          console.log('Query Success.');
        });
    },
    upload(val) {
      const path = 'http://localhost:5000/upload';
      axios.post(path, val)
        .then((response) => {
          const message = `\n Success! \n\n VERY IMPORTANT INFORMATION: \n
          Your private password is ${response.data.password}.\n
          You must remember it and use it to query the record. We will not keep it.\n
          And we will delete it forever.`;
          alert(message);
          console.log(response.data.password);
          console.log('Upload Success.');
        });
    },
    handleChange() {
      const fileInput = document.getElementById('fileInputCSV');
      this.papaParse(fileInput);
    },
    papaParse(obj) {
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
        // console.log(dp);
        this.backInput(dp);
      }, 1500);
      // this.backInput(results);
    },
    backInput(dp) {
      console.log(dp);
      this.features.forEach((feature) => {
        this.$set(this.input_values, feature, dp[0][feature]);
      });
    },
    queryBack(dp) {
      console.log(dp);
      this.features.forEach((feature, index) => {
        this.$set(this.input_values, feature, dp[index]);
      });
    },
    onsubmit() {
      const data = {
        ...this.input_values,
      };
      this.predict(data);
    },
    submitForQuery() {
      this.query(this.p_index);
    },
    submitForUpload() {
      const data = {
        ...this.input_values,
      };
      this.upload(data);
    },
  },
  async mounted() {
    this.features.forEach((feature) => {
      this.$set(this.input_values, feature, '');
    });
    const provider = await detectEthereumProvider();
    if (provider === window.ethereum) {
      window.ethereum.enable().then(() => {
      });
    } else {
      console.log(provider);
      alert('Please use MetaMask');
    }
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const currentAccounts = accounts[0];
    console.log(currentAccounts);
    if (currentAccounts !== '0xC50F355114394794Be1288544ebC6A3862d737fC') {
      alert('Please use a doctor account!');
      setTimeout(() => {
        router.replace({ path: 'patient' });
      }, 300);
    }
    window.ethereum.on('accountsChanged', (accounts1) => {
      // Time to reload your interface with accounts[0]!\
      console.log(accounts1[0]);
      if (accounts1[0] !== '0xC50F355114394794Be1288544ebC6A3862d737fC') {
        alert('Please use a doctor account!');
        setTimeout(() => {
          router.replace({ path: 'patient' });
        }, 300);
      }
    });
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
  display: flex;
  flex-direction: column;
  margin-top: 2em;
  margin-left: 2em;
}
.result_area {
  margin-top: 3em;
}
.button2 {
  margin-top: 0.5em;
}
.button3 {
  margin-top: 0.5em;
}
</style>
