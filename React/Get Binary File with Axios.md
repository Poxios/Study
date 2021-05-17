# Axios를 통한 바이너리 다운로드 작업 깨질 때 해결법
* GET으로 보안 Header을 이용해서 꼭 해야하는 상황에서 사용.
```tsx
  download: async (licenseId: string, user: any) =>
    axiosInstance.get(`/product/license/${licenseId}/key`, {
      ...getTokenHeader(await user.getIdToken()),
      responseType: "arraybuffer",
    }),
```
* `responseType: arraybuffer` 이게 중요하다
* https://stackoverflow.com/questions/62874303/rails-api-react-axios-downloads-corrupted-file