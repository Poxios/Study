# 기존의 styled-component 사용하는 것처럼 사용
* props=>props.selected와 같이 자유롭게 props를 사용하는, ThemeProvider을 사용해서까지 다크모드로 전환할 수 있는 컴포넌트들을 분리하기 위해서, 각 컴포넌트들을 분리한다.
```ts
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import {Theme} from '@material-ui/core';

export interface StyleProps {
    height: number;
}

const useStyles = makeStyles<Theme, StyleProps>(theme => ({
  root: {
    background: 'green',
    height: ({height}) => height,
  },
}));

export default function Hook() {

  const props = {
    height: 48
  }

  const classes = useStyles(props);
  return <Button className={classes.root}>Styled with Hook API</Button>;
}
```
