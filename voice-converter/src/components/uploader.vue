<style lang="scss">
  @import '../scss/icons';
</style>

<template>
  <icon-button name="save" class="ar-icon ar-icon__xs ar-icon--no-border" @click.native="upload"/>
</template>

<script>
  import IconButton from './icon-button'
  import UploaderPropsMixin from '../mixins/uploader-props'
  import Bus from '../assets/bus.js'

  export default {
    mixins: [UploaderPropsMixin],
    props: {
      record: { type: Object }
    },
    components: {
      IconButton
    },
    methods: {
      upload () {
        if (!this.record.url) {
          return
        }

        Bus.$emit('start-upload')

        const data = new FormData()
        data.append('audio', this.record.blob, `${this.filename}.mp3`)

        const headers = Object.assign(this.headers, {})
   
        this.$http.post(this.uploadUrl, data, { headers: headers }).then(resp => {
          Bus.$emit('end-upload', { status: 'success', response: resp })
        }).catch(error => {
          Bus.$emit('end-upload', { status: 'fail', response: error })
        })
      }
    }
  }
</script>
